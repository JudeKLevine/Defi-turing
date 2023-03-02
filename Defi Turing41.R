# Function to check if a number is prime
is_prime ‹- function(n) {
  if (n ‹ 2) {
    return(FALSE)
  }
  for (i in 2:sqrt(n)) {
    if (n %% i == 0) {
      return(FALSE)
    }
  }
  return(TRUE)
}

# Generate all pandigital numbers and check if they are prime
largest_pandigital_prime ‹- 0
for (i in 987654321:1) {
  if (is_prime(i) && all(sort(as.integer(strsplit(as.character(i), "")[[1]])) == 1:ceiling(log10(i)))) {
    largest_pandigital_prime ‹- i
    break
  }
}

print(largest_pandigital_prime)
