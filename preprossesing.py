#Preprossesing the dataset; resize, grayscale, adding label
#Splitting 80:20 into training and test
img_size = 128
def create_training_data():
    training_data = []
    for img in tqdm(real_path[:865]):
        path = os.path.join(real, img)
        label = [0] 
        image = cv2.resize( cv2.imread(path, cv2.IMREAD_GRAYSCALE), (img_size,img_size) )
        training_data.append([np.array(image), np.array(label)])
        
    for img in tqdm(fake_path[:768]):
        path = os.path.join(fake, img)
        label = [1] 
        image = cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE), (img_size,img_size))
        training_data.append([np.array(image), np.array(label)])

    shuffle(training_data)
    return(training_data)

#Creating a list of test data
def create_test_data():
    test_data = []
    for img in tqdm(real_path[865:]):
        path = os.path.join(real, img)
        label = [0] 
        image = cv2.resize( cv2.imread(path, cv2.IMREAD_GRAYSCALE), (img_size,img_size) )
        test_data.append([np.array(image), np.array(label)])
        
    for img in tqdm(fake_path[768:]):
        path = os.path.join(fake, img)
        label = [1] 
        image = cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE), (img_size,img_size))
        test_data.append([np.array(image), np.array(label)])

    shuffle(test_data)
    return(test_data)

train_data = create_training_data()
test_data = create_test_data()

#Seperating features and labels, to be able to feed into the model
train_img = []
train_lab = []
test_img = []
test_lab = []

for i in train_data:
    train_img.append(i[0])
    train_lab.append(i[1])
    
for i in test_data:
    test_img.append(i[0])
    test_lab.append(i[1])
    
#Reshape image 
train_img = np.array(train_img).reshape(-1, img_size, img_size, 1)
test_img = np.array(test_img).reshape(-1, img_size, img_size, 1)

#Divide by 255 to squish values to 0 - 1
train_img = train_img/255.0
train_lab = np.array(train_lab)

test_img = test_img/255.0
test_lab = np.array(test_lab)
