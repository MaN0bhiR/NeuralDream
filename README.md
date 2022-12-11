# NeuralDream

This is a project inspired by Neural Style Transfer Technique. It takes two images, a content Image and a style image from the user. The content image carries the core features that must be copied to the generated image, and the style image contains the low-level features like textures and shapes that must be copied onto the generated image. 

The idea is to extract the output of selected layers in the neural network and compare it with the outputs of the generated image, thereby calculating loss and updating generated Image.
Usually, the starting layers of Convolution layers have narrow features like edges and simple patterns, whereas the deeper layers have more sophisticated and specialized features. So the layer in the middle is chosen for the content features, and starting layer of all Conv layers are chosen for style features.
A pre-trained model named 'VGG-19' is used for extracting outputs for content and style, and the training involves iteratively updating the generated image by calculating loss.

The loss function is calculated from two components, content loss and style loss. The content loss is obtained by the difference between the outputs of the given content Image and generated image (output from the chosen content layer in the VGG 19 model). 
The style loss is obtained by passing the outputs of the style image and generated image through the gram matrix, which implies the correlation between outputs.

And then, I performed optimization to reduce the loss bewteen generated image and given images. The default train steps are set to 2000.

React is used for the frontend, and fetch API is used for making requests with the backend server. FastAPI is used in the backend to take input data from the user and run the whole algorithm and post the results back to the user after training.

Some of the output images are shown below.

![Dogs 2](https://user-images.githubusercontent.com/93503629/205932993-eecb8ce5-d4aa-4ed9-9c96-cb7db7662930.png)

![Screenshot_10](https://user-images.githubusercontent.com/93503629/205933072-28c0719a-c61c-4419-bbbc-634389feb63a.jpg)

![Screenshot_8](https://user-images.githubusercontent.com/93503629/205933262-9534efe5-e686-4284-8e76-5cbd55a224ad.jpg)

![Screenshot_4](https://user-images.githubusercontent.com/93503629/205933122-a566bc68-ab98-4ecb-970c-328a8943c5fe.jpg)

![Screenshot_3](https://user-images.githubusercontent.com/93503629/205933144-b82c71c8-adba-4bfa-9c6f-e598b0bccae9.jpg)
