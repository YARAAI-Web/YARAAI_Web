rule auto_rule_20250727013332_1644 {
  strings:
    $o0 = "pbmi" wide ascii nocase
    $o1 = "dword_43383B" wide ascii nocase
    $o2 = "pptl" wide ascii nocase
    $o3 = "ImageList_ReplaceIcon" wide ascii nocase
    $o4 = "x392F" wide ascii nocase
  condition:
    4 of ($o*)
}