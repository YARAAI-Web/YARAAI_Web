rule auto_rule_20250726181145_7749 {
  strings:
    $o0 = "GetLocaleInfoA" wide ascii nocase
    $o1 = "dword_455214" wide ascii nocase
    $o2 = "tail_loop_start" wide ascii nocase
  condition:
    3 of ($o*)
}