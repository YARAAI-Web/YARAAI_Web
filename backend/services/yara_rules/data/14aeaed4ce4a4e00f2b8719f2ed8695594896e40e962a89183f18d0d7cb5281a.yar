rule auto_rule_20250726110211_9032 {
  strings:
    $o0 = "dword_45C1C4" wide ascii nocase
    $o1 = "_bittestandset" wide ascii nocase
    $o2 = "__crtMessageBoxA" wide ascii nocase
    $o3 = "old_esp" wide ascii nocase
    $o4 = "byte_45CC14" wide ascii nocase
  condition:
    4 of ($o*)
}