rule auto_rule_20250726163623_4856 {
  strings:
    $o0 = "main_loop_0" wide ascii nocase
    $o1 = "_printMemBlockData" wide ascii nocase
  condition:
    all of them
}