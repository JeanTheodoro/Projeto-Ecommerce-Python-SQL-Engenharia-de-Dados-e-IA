from s3.connection import SupabaseS3Service

s3 = SupabaseS3Service()

files = s3.list_files()

for file in files:
    print(file)
