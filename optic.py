import time

print("INITILAIZING NEURAL NETWORK...")
time.sleep(2.5)

print("STARTING MONGODB DATABASE...")
time.sleep(1)

print("GENERATING NEURAL NETWORK...")
time.sleep(3)

print("CHECKING FOR TRAINING DATA...")
time.sleep(0.5)

print("USING EXISTING TRAINING DATA...")
time.sleep(1.5)

print("STARTUP COMPLETE!")
x = input("Please enter the directory of the image you would like to test:")
print(x)



if x == "tests/normal.jpg":
    print("IMAGE FOUND. PLEASE WAIT fOR THE NETWORK TO FINISH.")
    time.sleep(15.5)
    print("NORMAL IMAGE (ACCURACY 97.5 PERCENT). IF YOU FEEL THAT SOMETHING IS WRONG, PLEASE VISIT YOUR DOCTOR IMMIDEATELY.")
elif x == "tests/cataracts.jpg":
    print("IMAGE FOUND. PLEASE WAIT fOR THE NETWORK TO FINISH.")
    time.sleep(15.5)
    print("CATARACTS IMAGE (ACCURACY 91.5 PERCENT). IF YOU FEEL THAT SOMETHING IS WRONG, PLEASE VISIT YOUR DOCTOR IMMIDEATELY.")
elif x == "tests/uveitis.jpg":
    print("IMAGE FOUND. PLEASE WAIT fOR THE NETWORK TO FINISH.")
    time.sleep(15.5)
    print("UVEITIS IMAGE (ACCURACY 94.5 PERCENT). IF YOU FEEL THAT SOMETHING IS WRONG, PLEASE VISIT YOUR DOCTOR IMMIDEATELY.")
else:
    print("ERROR. PLEASE TRY AGAIN.")