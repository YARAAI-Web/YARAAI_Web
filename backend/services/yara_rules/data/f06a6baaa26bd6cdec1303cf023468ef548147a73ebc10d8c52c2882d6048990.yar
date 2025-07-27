rule auto_rule_20250726231958_7073 {
  strings:
    $o0 = "DdeConnectList" wide ascii nocase
    $o1 = "fInherit" wide ascii nocase
    $o2 = "hsz1" wide ascii nocase
    $o3 = "EnumDesktopsW" wide ascii nocase
    $o4 = "lpszFormat" wide ascii nocase
  condition:
    4 of ($o*)
}