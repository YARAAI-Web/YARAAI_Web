rule auto_rule_20250726205409_0185 {
  strings:
    $o0 = "pcchName" wide ascii nocase
    $o1 = "SHRegEnumUSValueW" wide ascii nocase
    $o2 = "fByPosition" wide ascii nocase
    $o3 = "ptszClassName" wide ascii nocase
    $o4 = "RegisterShellHookWindow" wide ascii nocase
  condition:
    4 of ($o*)
}