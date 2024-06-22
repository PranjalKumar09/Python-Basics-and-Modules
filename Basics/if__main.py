import tempmodule #You are welcome
#It will print above statement above even if do nothing
#because it is executing temp module

#to stop this such that it runs in temp module only when it
# is running on that file not when reported 
# so include-> if __name__ == "__main__":
#     in module file so that it will not run on other file
print(__name__) 