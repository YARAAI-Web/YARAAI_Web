rule auto_rule_20250726152218_9579 {
  strings:
    $o0 = "main_loop_0" wide ascii nocase
    $o1 = "byte_46ED61" wide ascii nocase
  condition:
    all of them
}