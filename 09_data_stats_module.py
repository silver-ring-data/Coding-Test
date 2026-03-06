def process_statistics(data_list):
  step1 = [(data + 10) for data in data_list if data >= 0 ] #데이터 가공

  step2 = list(map(lambda x : x**2, step1))

  return step2

def main():
    test_data = [-5, 2, 0, 10, -1]
    result = process_statistics(test_data)
    print(f"최종 결과: {result}")

if __name__ == '__main__':
  main()