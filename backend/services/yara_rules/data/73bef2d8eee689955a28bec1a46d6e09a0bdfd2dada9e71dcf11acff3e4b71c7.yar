rule auto_rule_20250726140225_2187 {
  strings:
    $o0 = "dword_42E2C4" wide ascii nocase
    $o1 = "dodwords" wide ascii nocase
    $o2 = "puTmpFileLen" wide ascii nocase
  condition:
    3 of ($o*)
}