#[macro_export]
macro_rules! info {
    ($($arg:tt)*) => {
        paris::output::format_stdout(format!("<blue>[INFO]</> {}", format!($($arg)*)), "\n")
    }
}

#[macro_export]
macro_rules! error {
    ($($arg:tt)*) => {
        paris::output::format_stdout(format!("<red>[ERROR]</> {}", format!($($arg)*)), "\n")
    }
}

#[macro_export]
macro_rules! warn {
    ($($arg:tt)*) => {
        paris::output::format_stdout(format!("<yellow>[WARN]</> {}", format!($($arg)*)), "\n")
    }
}
