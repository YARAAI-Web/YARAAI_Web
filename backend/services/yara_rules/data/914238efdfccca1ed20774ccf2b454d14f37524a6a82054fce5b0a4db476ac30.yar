rule auto_rule_20250726231735_5250 {
  strings:
    $o0 = "dword_44A044" wide ascii nocase
    $o1 = "main_loop_1" wide ascii nocase
  condition:
    all of them
}