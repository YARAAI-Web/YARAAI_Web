rule auto_rule_20250727031840_6869 {
  strings:
    $o0 = "PoolWithTag" wide ascii nocase
    $o1 = "dword_7F854" wide ascii nocase
    $o2 = "dword_7F788" wide ascii nocase
    $o3 = "swprintf" wide ascii nocase
  condition:
    4 of ($o*)
}