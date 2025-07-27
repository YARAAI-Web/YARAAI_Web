rule auto_rule_20250726160711_1571 {
  strings:
    $o0 = "WriteFileEx" wide ascii nocase
    $o1 = "ReadProcessMemory" wide ascii nocase
    $o2 = "lpCharacter" wide ascii nocase
    $o3 = "lphl" wide ascii nocase
  condition:
    4 of ($o*)
}