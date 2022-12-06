# NeuralDream

This is a project inspired by Neural Style Transfer Technique. It takes two images, a content Image and a style image from the user. The content image carries the core features that must be copied to the generated image, and the style image contains the low-level features like textures and shapes that must be copied onto the generated image. 

The idea is to extract the output of selected layers in the neural network and compare it with the outputs of the generated image, thereby calculating loss and updating generated Image.
Usually, the starting layers of Convolution layers have narrow features like edges and simple patterns, whereas the deeper layers have more sophisticated and specialized features. So the layer in the middle is chosen for the content features, and starting layer of all Conv layers are chosen for style features.
A pre-trained model named 'VGG-19' is used for extracting outputs for content and style, and the training involves iteratively updating the generated image by calculating loss.

The loss function is calculated from two components, content loss and style loss. The content loss is obtained by the difference between the outputs of the given content Image and generated image (output from the chosen content layer in the VGG 19 model). 
The style loss is obtained by passing the outputs of the style image and generated image through the gram matrix, which implies the correlation between outputs.

And then, I performed optimization to reduce the loss bewteen generated image and given images. The default train steps are set to 1000.

React is used for the frontend, and fetch API is used for making requests with the backend server. FastAPI is used in the backend to input the data from the user and run the whole algorithm and post the results back to the user after training.

Some of the output images are shown below.
