from google.cloud import vision

client = vision.ImageAnnotatorClient()
file_paths = [
  '/Users/user_a/Downloads/recipe01.jpeg',
  '/Users/user_a/Downloads/recipe02.jpeg',
  '/Users/user_a/Downloads/recipe03.jpeg',
  '/Users/user_a/Downloads/recipe04.jpeg'
]

output_text = ''

for file_path in file_paths:
  with open(file_path, 'rb') as image_file:
    content = image_file.read()

  image = vision.Image(content=content)

  response = client.document_text_detection(
    image=image,
    image_context={'language_hints': ['ja']}
  )
  output_text += response.full_text_annotation.text + '\n'

print(output_text)
