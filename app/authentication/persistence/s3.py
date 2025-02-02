import boto3
import uuid

# Configuración de S3
s3_client = boto3.client("s3")
BUCKET_NAME = "my-s3-bucket"

def upload_file_to_s3(file, filename):
    """
    Sube un archivo a S3.
    """
    file_id = str(uuid.uuid4())
    s3_client.upload_fileobj(file.file, BUCKET_NAME, file_id)
    return {"file_id": file_id}

def download_file_from_s3(file_id):
    """
    Genera un enlace para descargar un archivo desde S3.
    """
    return s3_client.generate_presigned_url(
        "get_object", Params={"Bucket": BUCKET_NAME, "Key": file_id}, ExpiresIn=3600
    )

def delete_file_from_s3(file_id):
    """
    Elimina un archivo en S3.
    """
    s3_client.delete_object(Bucket=BUCKET_NAME, Key=file_id)
