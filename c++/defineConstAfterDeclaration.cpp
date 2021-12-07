#include <iostream>
const extern int i;

int main() {
  // define the const i only once after declaration
  const int i = [](){
       return 10;
  }();

  std::cout << i << "\n";

  try {
    // This crashes as you can tell by i still being 10 in the second print
    const int i = [](){ // init
         return 20;
    }();
  } catch (const std::exception&) {
  }
  
  std::cout << i << "\n";
  return 0;
}
