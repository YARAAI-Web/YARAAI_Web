rule auto_rule_20250726182321_9667 {
  strings:
    $o0 = "x1004u" wide ascii nocase
    $o1 = "copy_start" wide ascii nocase
    $o2 = "off_47632C" wide ascii nocase
    $o3 = "_controlfp" wide ascii nocase
  condition:
    4 of ($o*)
}