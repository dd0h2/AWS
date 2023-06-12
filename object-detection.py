import boto3
import csv
from PIL import Image, ImageDraw, ImageFont
import io

#자격 증명 파일을 여는 프로그램
with open('credentials.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)

#자격증명 얻기
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

#aws rekognition sdk 연결
client = boto3.client('rekognition', region_name='ap-northeast-2', 
                        aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

#사진 받기
photo = '1593753545389.jpg'

with open(photo, 'rb') as source image_file: 
        source_bytes = image_file.read()

#사진 감지
detect_objects = client.detect_labels(Image={'Bytes': source_bytes})
print(detect_objects)

#네모박스 표시
image = Image.open(io.BytesIO(source_bytes))
draw = ImageDraw.Draw(image)
    
for label in detect_objects['Labels']:
    print(label["Name"])
    print("Confidence: ", label["confidence"] )
    
    for instances in label['Instances']:
        if 'BoundingBox' in instances:
            
            box = instances["BoundingBox"]
            
            left = image.width*box['Left']
            top = image.height*box['Top']
            width = image.width*box['Width']
            height = image.height*box['Height']
            
            points = (
                        (left,top),
                        (left + width, top),
                        (left + width, top + height),
                        (left, top + height),
                        (left, top)
                    )
            draw.line(points, width=5, fill = "#eb34db")
            
        
image.show()
    