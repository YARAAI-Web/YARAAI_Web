rule auto_rule_20250726131003_7563 {
  strings:
    $o0 = "uMsg" wide ascii nocase
    $o1 = "cchClassNameMax" wide ascii nocase
    $o2 = "RegOpenKeyA" wide ascii nocase
    $o3 = "LockWorkStation" wide ascii nocase
    $o4 = "BlockInput" wide ascii nocase
  condition:
    4 of ($o*)
}