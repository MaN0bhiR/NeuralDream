import NeuralArt
from NeuralArt import train_step , generate_target , imshow ,  tensor_to_image
import time
import PIL.Image as Image
import io


def start_training(content_path , style_path):

  image , target = generate_target(content_path=content_path , style_path=style_path)
  import time
  start = time.time()
  epochs = 10
  steps_per_epoch = 5
  current_step = 0
  for n in range(epochs):
    for m in range(steps_per_epoch):
      current_step+=1
      train_step(image , target)
      print(".", end='', flush=True)
    image_PIL = tensor_to_image(image)
    with io.BytesIO() as buf:
                image_PIL.save(buf, format='PNG')
                image_bytes = buf.getvalue()
    yield image_bytes
    print(f"Train Step: {current_step}")
  end = time.time()
  print(f'Total time consumed is {end-start}')


