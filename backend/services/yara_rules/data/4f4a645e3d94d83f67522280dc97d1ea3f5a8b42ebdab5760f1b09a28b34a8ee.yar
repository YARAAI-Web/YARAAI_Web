rule auto_rule_20250726231502_9547 {
  strings:
    $o0 = "byte_4070DD" wide ascii nocase
    $o1 = "byte_40725F" wide ascii nocase
    $o2 = "dword_405734" wide ascii nocase
    $o3 = "byte_40715B" wide ascii nocase
  condition:
    4 of ($o*)
}