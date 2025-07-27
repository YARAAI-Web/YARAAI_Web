rule auto_rule_20250726194624_3970 {
  strings:
    $o0 = "dword_42E8D1" wide ascii nocase
    $o1 = "dword_42E8A1" wide ascii nocase
    $o2 = "dword_42D048" wide ascii nocase
  condition:
    3 of ($o*)
}