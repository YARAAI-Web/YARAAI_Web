rule auto_rule_20250727012021_9620 {
  strings:
    $o0 = "dword_782E8" wide ascii nocase
    $o1 = "dword_78450" wide ascii nocase
    $o2 = "word_1E61A" wide ascii nocase
    $o3 = "dword_777B4" wide ascii nocase
  condition:
    4 of ($o*)
}