from PySide6.QtCore import QThread, Signal, QByteArray
import paramiko
from io import BytesIO

class DataFetcher(QThread):
    data_fetched = Signal(dict, QByteArray)
    image_fetched = Signal(QByteArray)
    error_occurred = Signal(str)

    def __init__(self, mongo_db_instance, match_id, ssh_details, parent=None):
        super().__init__(parent)
        self.mongo_db_instance= mongo_db_instance
        self.match_id = match_id
        self.ssh_details = ssh_details

    def run(self):
        try:
            match_data = self.fetch_match_data()
            image_data = self.fetch_image_data(match_data)
            if match_data and image_data is not None:
                self.data_fetched.emit(match_data, QByteArray(image_data))
            else:
                self.error_occurred.emit("Failed to fetch match data or image.")
        except Exception as e:
            self.error_occurred.emit(str(e))

    def fetch_match_data(self):
        match_data = self.mongo_db_instance.find_match_by_id_and_moves_not_validated(self.match_id)
        if not match_data:
            raise ValueError("Match data not found.")
        return match_data


    def fetch_image_data(self, match_data):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(**self.ssh_details)

        sftp = ssh_client.open_sftp()
        first_move = match_data.get('moves', [{}])[0]
        file_path = first_move.get('file')
        image_data = None
        if file_path:
            with BytesIO() as fl:
                sftp.getfo(file_path, fl)
                fl.seek(0)
                image_data = fl.read()

        sftp.close()
        ssh_client.close()

        return QByteArray(image_data)


    def fetch_next_image(self, move):
        """Fetches the image corresponding to a move."""
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(**self.ssh_details)

            with BytesIO() as fl:
                with ssh_client.open_sftp() as sftp:
                    sftp.getfo(move['file'], fl)
                    fl.seek(0)
                    image_data = fl.read()

            # Emit the signal with the image data
            self.image_fetched.emit(QByteArray(image_data))

            ssh_client.close()
        except Exception as e:
            self.error_occurred.emit(str(e))

