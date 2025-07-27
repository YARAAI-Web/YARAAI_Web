rule auto_rule_20250726124523_9424 {
  strings:
    $o0 = "dword_4795F8" wide ascii nocase
    $o1 = "CopyUnwindUp_0" wide ascii nocase
    $o2 = "dword_431230" wide ascii nocase
    $o3 = "dword_4798A8" wide ascii nocase
  condition:
    4 of ($o*)
}