rule auto_rule_20250726132236_9080 {
  strings:
    $o0 = "uItem" wide ascii nocase
    $o1 = "IsBadStringPtrA" wide ascii nocase
    $o2 = "GetUserObjectSecurity" wide ascii nocase
    $o3 = "OpenEventW" wide ascii nocase
    $o4 = "lstrlenW" wide ascii nocase
  condition:
    4 of ($o*)
}