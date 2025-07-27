rule auto_rule_20250726141823_8447 {
  strings:
    $o0 = "off_49DDB4" wide ascii nocase
    $o1 = "word_4C10F0" wide ascii nocase
    $o2 = "TaskbarCreated" wide ascii nocase
    $o3 = "dword_4C1684" wide ascii nocase
  condition:
    4 of ($o*)
}