class GameManager:
    def __init__(self, city, processor, report_service):
        self.city = city
        self.processor = processor
        self.report_service = report_service
        self.turn = 1

    def run_turn(self, instructions):
        balance, growth, completed = self.processor.process_turn(
            self.city, instructions
        )

        report = self.report_service.generate(
            self.city, balance, growth
        )

        self.turn += 1
        return report

