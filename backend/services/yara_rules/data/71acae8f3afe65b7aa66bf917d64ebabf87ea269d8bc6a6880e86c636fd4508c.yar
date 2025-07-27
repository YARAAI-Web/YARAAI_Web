rule auto_rule_20250726191201_9355 {
  strings:
    $o0 = "dword_445E98" wide ascii nocase
    $o1 = "dword_445AB0" wide ascii nocase
    $o2 = "dword_407000" wide ascii nocase
  condition:
    3 of ($o*)
}