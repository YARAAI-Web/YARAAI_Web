rule auto_rule_20250726122941_9798 {
  strings:
    $o0 = "dword_44A3B8" wide ascii nocase
    $o1 = "tail_loop_start" wide ascii nocase
    $o2 = "dword_44A048" wide ascii nocase
  condition:
    3 of ($o*)
}