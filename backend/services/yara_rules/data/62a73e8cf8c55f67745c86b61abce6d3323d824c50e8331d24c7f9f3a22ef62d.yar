rule auto_rule_20250727010851_9481 {
  strings:
    $o0 = "PathCompactPathExW" wide ascii nocase
    $o1 = "GetSystemMenu" wide ascii nocase
    $o2 = "StrRetToBufA" wide ascii nocase
    $o3 = "pcchMaxSubKeyLen" wide ascii nocase
    $o4 = "GetSubMenu" wide ascii nocase
  condition:
    4 of ($o*)
}