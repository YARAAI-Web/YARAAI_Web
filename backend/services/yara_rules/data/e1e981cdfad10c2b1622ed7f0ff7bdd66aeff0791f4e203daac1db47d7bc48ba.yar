rule auto_rule_20250727000833_3163 {
  strings:
    $o0 = "SetComputerNameExA" wide ascii nocase
    $o1 = "GetAncestor" wide ascii nocase
    $o2 = "hWndMain" wide ascii nocase
    $o3 = "ImageList_DragEnter" wide ascii nocase
  condition:
    4 of ($o*)
}