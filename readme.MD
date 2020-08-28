# Damage Detection on Cars using Deflectometry & Computer Vision

## Overview
A project where we detect various classes of damage on cars moving through a device constructed to photgraph slow moving cars that pass through it. This device is already deployed at several locations of Merecedes Benz dealerships in Germany. We have image data from these locations, some labeled with damage. Our goal is to create a model that can detect damage, classify it, and create a bounding box of the damage location. The device has deflectometry pattern display screens which are commonly used for solving this kind of task.

# Data

## Image Examples

### Dach
<table>
  <tr>
    <td>Links</td>
    <td>Rechts</td>
  </tr>
  <tr>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00190.jpg"></td>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Rechts-_00170.jpg"></td>
  </tr>
  <tr>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00194.jpg"></td>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Rechts-_00174.jpg"></td>
  </tr>
 <tr>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00194.jpg"></td>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00201.jpg"></td>
  </tr>
</table>

### Front
<table>
  <tr>
    <td colspan="2">Nah</td>
   <td colspan="2">Weit</td>
  </tr>
  <tr>
    <td>Links</td>
    <td>Rechts</td>
    <td>Links</td>
    <td>Rechts</td>
  </tr>
  <tr>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Front/2020-07-18%2B17-21-47%2BALU4567-Front%2BNah%2BLinks-_00023.jpg"></td>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Front/2020-07-18%2B17-21-47%2BALU4567-Front%2BNah%2BRechts-_00020.jpg"></td>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Front/2020-07-18%2B17-21-47%2BALU4567-Front%2BWeit%2BLinks-_00313.jpg"></td>
    <td><img width="300" alt="car_img" src="Data-CarPictures/Front/2020-07-18%2B17-21-47%2BALU4567-Front%2BWeit%2BRechts-_00310.jpg"></td>
  </tr>
</table>

### Heck
| Links| Rechts|
|:-------------------------:|:-------------------------:|
|<img width="1604" alt="car_img_1" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00190.jpg"> 1 |  <img width="1604" alt="car_img_2" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Front%2BWeit%2BRechts-_00311.jpg"> 2 |
|<img width="1604" alt="car_img_4" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BUnten-_00059.jpg"> 3 |  <img width="1604" alt="car_img_5" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BMitte-_00080.jpg"> 4 |

### Schweller
| Links| Rechts|
|:-------------------------:|:-------------------------:|
|<img width="1604" alt="car_img_1" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00190.jpg"> 1 |  <img width="1604" alt="car_img_2" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Front%2BWeit%2BRechts-_00311.jpg"> 2 |
|<img width="1604" alt="car_img_4" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BUnten-_00059.jpg"> 3 |  <img width="1604" alt="car_img_5" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BMitte-_00080.jpg"> 4 |

### Seite
| Links| Rechts|
|:-------------------------:|:-------------------------:|
|<img width="1604" alt="car_img_1" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00190.jpg"> 1 |  <img width="1604" alt="car_img_2" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Front%2BWeit%2BRechts-_00311.jpg"> 2 |
|<img width="1604" alt="car_img_4" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BUnten-_00059.jpg"> 3 |  <img width="1604" alt="car_img_5" src="pictures/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BMitte-_00080.jpg"> 4 |

### Image Variability

#### Movement
8 km/hr movement through scanner allowed
Sometimes users drive faster than that

#### Data Changes
 Varied lighting conditions
 Varied Cars Brands
 
## Remote Server

```ssh username@1.2tronic.biz -p 7722```

## Storage Share Database Folder Layout

[Storage Share Website](https://nx11096.your-storageshare.de/apps/files/?dir=/ADA&fileid=2035778)

* ADA
* * Asperg (a)
* * Ellgau (a)
* * Essen (a)
* * KI
* * * First Step Ordner
* * *  Quick Check Daten
* * Marker
* * * Bialek
* * * Eisfeld
* * * Felix
* * * * N0U101
* * * * * {date}
* * * * * * {time}
* * * * * * * face
* * * * * * * thumbnails
* * * * * * * {img-name} (96 files)
* * * * ...(5 more)
* * * Hakobyan
* * * Marker1
* * * Theodor
* * * Theodor1
* * * Victor
* * Nuernberg (a)
* * Stuttgart (a)

Folder Structure (a) - Damage Reports

* * * corrosion
* * * crack
* * * deformation
* * * dent bump
* * * dirt
* * * misc
* * * no damage
* * * reflection
* * * rim damage
* * * scratch
* * * vehicle

## Hardware

### Cameras
6 Cameras - 2-3 photos for each - 4k resolution
6 * 3 * 3840*2160 = 149,299,200 pixels per scan

### Proposed
Relectometry


# Use Case

## Customers

* Mercedes Sellers
Their customers take a weekend test drive in their Mercedes.
This device checks for scratches when the customer returns it.

* Repair Stations

* Factory Line Damage Check

* Leasing companies

* Rental car companies
