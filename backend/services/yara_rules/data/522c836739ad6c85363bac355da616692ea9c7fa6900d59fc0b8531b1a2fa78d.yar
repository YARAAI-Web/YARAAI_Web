rule auto_rule_20250727034345_0034 {
  strings:
    $o0 = "lpDef" wide ascii nocase
    $o1 = "dwVer" wide ascii nocase
    $o2 = "InternalGetWindowText" wide ascii nocase
    $o3 = "uMsg" wide ascii nocase
    $o4 = "uSizeStruct" wide ascii nocase
  condition:
    4 of ($o*)
}