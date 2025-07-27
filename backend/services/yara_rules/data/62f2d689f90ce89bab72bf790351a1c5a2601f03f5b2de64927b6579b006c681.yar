rule auto_rule_20250726234346_4429 {
  strings:
    $o0 = "dword_4643D8" wide ascii nocase
    $o1 = "main_loop_0" wide ascii nocase
    $o2 = "_pLastBlock" wide ascii nocase
  condition:
    3 of ($o*)
}