# NeuralDream

This is a project inspired from Neural Style Transfer Technique.It takes two images , a content Image and a style image from the user. The content image carries the core features that has to be copied to generated image and style image contains the low level features like textures and shape that has to copied onto the generated image. 

The idea is to extract the output of selected layers in neural network and compare it with outputs of generated image , thereby calculating loss and updating generated Image.
Usually , the starting layers if Convolution layers have narrow features like edges and simple patters where as the deeper layers have more sophisticated and specialized features. So the layer in the middle is choosen for the content features and starting layer of all conv layers are chosen for style features.
A pretrained model named 'VGG-19' is used for extracting outputs for content and style and the training involves iteratively updating the generated image by calculating loss.

The loss function is calculated from two components , content loss and style loss. The content loss is obtained by differnece between outputs of given content Image and generated Image (output from chosen content layer in VGG 19 model) . 
The style loss is obtained by passing the outputs of style image and generated image through gram matrix which implies the correlation between outputs.

And then I performed optimization to reduce the loss bewteen  generated image and given images.The default train steps are set to 1000.

React is used for frontend and fetch API used for making request with backend server. FastAPI is in the backend to input the data from user and run the whole algorithm and post the results back to user after training.

Some of the output images are shown below.
