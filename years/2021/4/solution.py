from common.solution import Solution


class Day(Solution):
    def parse_bingo(self):
        lines = self.data
        numbers = [int(x) for x in lines[0].split(",")]

        boards = []
        board_maps = []
        current_board = []
        current_map = []

        for i in range(2, len(lines)):
            line = lines[i]
            if line.strip():
                nums = [int(s) for s in line.split() if s.strip()]
                current_board.append(nums)
                current_map.append([False] * 5)

                if len(current_board) == 5:
                    boards.append(current_board)
                    board_maps.append(current_map)
                    current_board = []
                    current_map = []

        return numbers, boards, board_maps

    def check_col(self, board_map, col):
        for k in range(5):
            if not board_map[k][col]:
                return False
        return True

    def part1(self):
        numbers, boards, board_maps = self.parse_bingo()

        for number_drawn in numbers:
            for board_idx in range(len(boards)):
                table = boards[board_idx]
                mappsy = board_maps[board_idx]
                for row in range(len(table)):
                    for col in range(len(table[row])):
                        if table[row][col] == number_drawn:
                            mappsy[row][col] = True
                            row_sum = sum(mappsy[row])
                            if row_sum == 5 or self.check_col(mappsy, col):
                                # Calculate sum of unmarked
                                s = 0
                                for r in range(len(table)):
                                    for k in range(len(table[r])):
                                        if not mappsy[r][k]:
                                            s += table[r][k]
                                return s * number_drawn
        return 0

    def has_bingo(self, grid, row, col):
        col_has_bingo = True
        for i in range(5):
            if not grid[i][col]:
                col_has_bingo = False

        return sum(grid[row]) == 5 or col_has_bingo

    def part2(self):
        numbers, boards, board_maps = self.parse_bingo()

        total_rounds = []

        for board_idx in range(len(boards)):
            board = boards[board_idx]
            numbers_drawn = 0

            for current_drawn in numbers:
                won = False
                for row in range(len(board)):
                    for col in range(5):
                        if board[row][col] == current_drawn:
                            board_maps[board_idx][row][col] = True

                            if self.has_bingo(board_maps[board_idx], row, col):
                                total_rounds.append(
                                    [numbers_drawn, current_drawn, board_idx]
                                )
                                won = True
                                break
                    if won:
                        break
                if won:
                    break
                numbers_drawn += 1

        max_value = max(total_rounds)
        board_idx = max_value[2]
        last_number = max_value[1]

        s = 0
        for r in range(len(boards[board_idx])):
            for k in range(len(boards[board_idx][r])):
                if not board_maps[board_idx][r][k]:
                    s += boards[board_idx][r][k]

        return s * last_number


Day().solve()
