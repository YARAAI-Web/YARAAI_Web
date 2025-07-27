rule auto_rule_20250727024838_0718 {
  strings:
    $o0 = "FlatSB_GetScrollPos" wide ascii nocase
    $o1 = "SetVolumeLabelA" wide ascii nocase
    $o2 = "uFormat" wide ascii nocase
    $o3 = "lpOverlapped" wide ascii nocase
    $o4 = "UserHandleGrantAccess" wide ascii nocase
  condition:
    4 of ($o*)
}