rule auto_rule_20250726114617_3697 {
  strings:
    $o0 = "dword_44A030" wide ascii nocase
    $o1 = "main_loop_entrance" wide ascii nocase
  condition:
    all of them
}