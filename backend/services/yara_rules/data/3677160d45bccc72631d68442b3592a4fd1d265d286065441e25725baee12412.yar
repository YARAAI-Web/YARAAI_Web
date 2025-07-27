rule auto_rule_20250727031310_4275 {
  strings:
    $o0 = "kr04_2" wide ascii nocase
    $o1 = "dword_1EB64" wide ascii nocase
    $o2 = "x22C038" wide ascii nocase
    $o3 = "RtlImageNtHeader" wide ascii nocase
    $o4 = "dword_7F5A8" wide ascii nocase
  condition:
    4 of ($o*)
}