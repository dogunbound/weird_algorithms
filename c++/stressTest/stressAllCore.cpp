#include <thread>
#include <list>
#include <iostream>
#include <string>



int slammerFunc() {
  while(true) {
    const int randomNum = rand() % 1000000000 + 1000000000;

    int m = randomNum / 2;
    bool isPrime = true;
    for (int i = 2; i <= m; i++) {
      if (randomNum % i == 0) {
        isPrime = false;
        break;
      }
    }

   if (isPrime) {
     std::cout << randomNum << " is a prime number!" << std::endl;
   }
  }

  return 0;
}

bool isNumber(const std::string& str)
{
    for (char const &c : str) {
        if (std::isdigit(c) == 0) return false;
    }
    return true;
}

int main(int argc, char *argv[]) {
  if (argc < 2 || !isNumber(argv[1])) {
    std::cout << "You need to indicate the number of threads you want to slam\nExample command: ./stress 16\nIndicates to stress 16 cores\n";

    return 1;
  }

  int numCores = std::stoi(argv[1]);
  std::list<std::thread> listOfThreads = std::list<std::thread>();
  for (int i = 0; i < numCores; i++) {
    listOfThreads.push_back(std::thread(slammerFunc));
  }

  for (auto& i : listOfThreads) {
    i.join();
  }

  return 0;
}
