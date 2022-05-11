struct Example {
  msg: String,
  num: u32,
}

impl Example {
    fn new<T: ExampleInit>(arg: T) -> Example {
        arg.__new_example()
    }
}

trait ExampleInit {
    fn __new_example(self) -> Example;
}

impl ExampleInit for u32 {
    fn __new_example(self) -> Example {
        Example {
            msg: String::new(),
            num: self,
        }
    }
}

impl ExampleInit for String {
    fn __new_example(self) -> Example {
        Example {
            msg: self,
            num: 0,
        }
    }
}

fn main() {
  let msg = Example::new(String::from("msg")); // num = 0
  let num = Example::new(32); // msg = ""

}
