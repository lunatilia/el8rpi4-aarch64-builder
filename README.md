## c8rpi4-aarch64-builder

### 内容
c8rpi4-aarch64-builder は、下記のカスタムディスクイメージを作成するスクリプトです。  
※2021年05月02日現在、Raspberry Pi 用の CentOS Userland 8 公式ディスクイメージは公開されていないようです。

- CentOS Userland 8 for Raspberry Pi 4 (aarch64)
- CentOS Userland 8 Stream for Raspberry Pi 4 (aarch64)

### 要件
- CentOS 8 (aarch64) が稼働している Raspberry Pi 4 Model B
    - [CentOS - Raspberry PI 4 - CentOS Forums](https://forums.centos.org/viewtopic.php?f=55&t=73495)
    - [開発者によるテスト用ディスクイメージ](https://people.centos.org/pgreco/CentOS-Userland-8-stream-aarch64-RaspberryPI-Minimal-4/)
- 4 GB 以上の microSD (16 GB以上を推奨)
- root権限
- git、lorax-lmc-novirt、patch および依存パッケージ
- 別途ビルドした raspberrypi2-kernel4、raspberrypi2-firmware パッケージ
  - epel-release、mock および依存パッケージ

### srpm からのカーネルビルドと、ディスクイメージ作成の実行例

#### 準備

```
# yum install git patch lorax-lmc-novirt epel-release
# git clone https://github.com/lunatilia/c8rpi4-aarch64-builder
# cd c8rpi4-aarch64-builder
# yum install mock
# usermod -a -G mock <user>
# mkdir -p /centos/8/{SRPMS,aarch64}
```

#### srpm からの raspberrypi2 のビルド

- raspberrypi2-5.10.29-v8.1.el8.src.rpm は、ソースから事前に作成
  - source : https://git.centos.org/rpms/raspberrypi2/tree/c7-sig-altarch-lts-5-10

```
# setenforce 0
$ mock -r centos-stream-8-aarch64 --init
$ mock -r centos-stream-8-aarch64 rebuild raspberrypi2-5.10.29-v8.1.el8.src.rpm
# mv /var/lib/mock/centos-stream-8-aarch64/result/*.src.rpm /centos/8/SRPMS/
# mv /var/lib/mock/centos-stream-8-aarch64/result/*.rpm /centos/8/aarch64/
$ mock -r centos-stream-8-aarch64 --clean
# setenforce 1
# createrepo /centos/8/aarch64/
```

#### ディスクイメージ作成

- CentOS 8 の場合

```
# ./c8rpi4-aarch64-builder kickstarts/c8rpi4-minimal-ks.cfg
```

- CentOS Stream 8 の場合

```
# ./c8srpi4-aarch64-builder kickstarts/c8srpi4-minimal-ks.cfg
```

### ディスクイメージ
- [ディスクイメージのダウンロード](https://github.com/lunatilia/c8rpi4-aarch64-builder/releases/tag/0.3.0-20210502)

### ライセンス
[GNU General Public License v2.0](https://github.com/lunatilia/c8rpi4-aarch64-builder/blob/master/LICENSE) (The CentOS Projectのデフォルトライセンス)

### 参考

#### raspberrypi2 のソース

- [rpms / raspberrypi2 - git.centos.org](https://git.centos.org/rpms/raspberrypi2)
