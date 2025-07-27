rule auto_rule_20250726161939_9552 {
  strings:
    $o0 = "ExRaiseStatus" wide ascii nocase
    $o1 = "dword_7ED7C" wide ascii nocase
    $o2 = "ZwMapViewOfSection" wide ascii nocase
  condition:
    3 of ($o*)
}