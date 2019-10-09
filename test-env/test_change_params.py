from abstract_test import AbstractTest


class BasicTests(AbstractTest):
    def test1(self):
        self.env.run_icommand(0, ["ip", 'a', 's'])

        self.env.run_icommand(0, ["ping", "-c", "4", self.env.get_node_ip(1)])

        self.env.add_net_params([0, 1], 0, {'delay': ['200ms']})

        self.env.run_icommand(0, ["ping", "-c", "4", self.env.get_node_ip(1)])

        self.env.set_net_params([0, 1], 0, {'delay': ['100ms']})

        self.env.run_icommand(0, ["ping", "-c", "4", self.env.get_node_ip(1)])

        self.env.set_net_params([0, 1], 0, {'delay': ['0ms']})

        self.env.run_icommand(0, ["ping", "-c", "4", self.env.get_node_ip(1)])

        self.env.finish()


if __name__ == "__main__":
    basic_tests = BasicTests("c3.json")
    basic_tests.test1()
