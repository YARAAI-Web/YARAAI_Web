rule auto_rule_20250727032823_1404 {
  strings:
    $o0 = "RemovePropW" wide ascii nocase
    $o1 = "GetWindowWord" wide ascii nocase
    $o2 = "lstrcatA" wide ascii nocase
    $o3 = "dwCreationDisposition" wide ascii nocase
  condition:
    4 of ($o*)
}