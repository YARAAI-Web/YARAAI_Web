rule auto_rule_20250726190637_0618 {
  strings:
    $o0 = "main_loop_entrance_0" wide ascii nocase
    $o1 = "off_455CEC" wide ascii nocase
  condition:
    all of them
}